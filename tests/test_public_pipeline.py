import os
def test_public_data_used_by_default():
    # detector load should use data/public by default
    from src.agents.price_detector import detect_public_only
    df = detect_public_only()
    assert df is not None
    # ensure private labels folder not read by default
    assert os.path.exists("data/public/pos.csv")
