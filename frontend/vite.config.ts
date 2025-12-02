import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
      },
      '/UI_ENHANCEMENT_PLAN.md': {
        target: 'http://127.0.0.1:8000/UI_ENHANCEMENT_PLAN.md',
        changeOrigin: true,
      }
    }
  }
})
