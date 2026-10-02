import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 11000,
    proxy: {
      '/api': {
        target: 'http://localhost:11001',
        changeOrigin: true,
      },
    },
  },
})
