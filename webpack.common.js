const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const Dotenv = require('dotenv-webpack');

module.exports = {
  entry: [
    './src/front/js/index.js'
  ],
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'public'),
    publicPath: '/'
  },
  module: {
    rules: [
        {
          test: /\.(js|jsx)$/,
          exclude: /node_modules/,
          use: ['babel-loader']
        },
        {
          test: /\.(css|scss)$/, 
          use: ['style-loader', 'css-loader']
        },
        {
          test: /\.(png|svg|jpg|gif|jpeg|webp)$/, 
          use: {
            loader: 'file-loader',
            options: { name: '[name].[ext]' }
          }
        }
    ]
  },
  resolve: {
    extensions: ['*', '.js', '.jsx']
  },
  plugins: [
    new HtmlWebpackPlugin({
        template: 'template.html'
    }),
    new Dotenv({ safe: true, systemvars: true })
  ]
};