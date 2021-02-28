export default {
    // "build": "vite build && rm -r ../www/* && cp -r ./dist/* ../www && rm -r ./dist/* && cp -r ../www/www/* ../www&& rm -r ../www/www"
  // assetsDir: 'www',
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