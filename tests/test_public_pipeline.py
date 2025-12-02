import sys
import os
import pandas as pd
from sqlalchemy import create_engine
from src.agents.price_detector import detect_public_only

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_public_data_used_by_default(monkeypatch):
    # Create an in-memory SQLite database
    engine = create_engine('sqlite:///:memory:')

    # Create test data
    pos_data = {'po_id': [1, 2, 3, 4, 5],
                'contract_id': [1, 1, 2, 2, 3],
                'unit_price': [110, 100, 205, 200, 300]}
    pos_df = pd.DataFrame(pos_data)
    pos_df.to_sql('pos', engine, index=False)

    contracts_data = {'contract_id': [1, 2],
                      'contract_unit_price': [100, 200]}
    contracts_df = pd.DataFrame(contracts_data)
    contracts_df.to_sql('contracts', engine, index=False)

    # Use monkeypatch to point the price_detector's engine to the in-memory DB
    monkeypatch.setattr('src.agents.price_detector.engine', engine)

    df = detect_public_only()
    
    assert df is not None
    assert len(df) == 1
    assert df['po_id'].tolist() == [1]
    # Re-calculate drift as a float for accurate comparison
    assert df['price_drift'].iloc[0] == 1.1

def test_drift_threshold_parameter(monkeypatch):
    # Create an in-memory SQLite database
    engine = create_engine('sqlite:///:memory:')

    # Create test data
    pos_data = {'po_id': [1, 2, 3, 4, 5],
                'contract_id': [1, 1, 2, 2, 3],
                'unit_price': [110, 100, 205, 200, 300]}
    pos_df = pd.DataFrame(pos_data)
    pos_df.to_sql('pos', engine, index=False)

    contracts_data = {'contract_id': [1, 2],
                      'contract_unit_price': [100, 200]}
    contracts_df = pd.DataFrame(contracts_data)
    contracts_df.to_sql('contracts', engine, index=False)

    # Use monkeypatch to point the price_detector's engine to the in-memory DB
    monkeypatch.setattr('src.agents.price_detector.engine', engine)

    # Test with a higher threshold
    df = detect_public_only(drift_threshold=15)
    
    assert df is not None
    assert len(df) == 0

    # Test with a lower threshold
    df = detect_public_only(drift_threshold=2)

    assert df is not None
    assert len(df) == 2
    assert df['po_id'].tolist() == [1, 3]
    assert df['price_drift'].iloc[0] == 1.1
    assert df['price_drift'].iloc[1] == 1.025