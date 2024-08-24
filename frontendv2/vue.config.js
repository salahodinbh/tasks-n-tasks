module.exports = {
  devServer: {
    proxy: {
      // For some reason, the proxy is not working properly.
      // I'll just proceed using the plain localhost url for now.
      '/api': {
        target: 'http://localhost:5000a/',
        changeOrigin: true
      },
    },
  },
};
