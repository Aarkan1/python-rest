export default {
    proxy: {
      '/rest': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        // rewrite: path => path.replace(/^\/api/, '')
      },
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true,
        // rewrite: path => path.replace(/^\/api/, '')
      }
    }
  }