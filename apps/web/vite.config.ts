import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 10000,
    proxy: {
      '/api': {
        target: 'http://localhost:10001',
        changeOrigin: true,
      },
    },
  },
})
