gulp = require('gulp-help') require 'gulp'
browserSync = require('browser-sync')
$ = require('gulp-load-plugins')()
config = require '../config'
paths = require '../paths'


gulp.task 'browser-sync', false, ->
  browserSync.init
    proxy: "#{config.host}:#{config.port}"
    notify: false
    open: false
  $.watch [
    "#{paths.main}/**/*.{html,py}"
  ], events: ['change'], (file) ->
    browserSync.reload()


gulp.task 'watch', false, ->
  $.watch 'requirements.txt', ->
    $.sequence('pip')()
  $.watch 'package.json', ->
    $.sequence('npm')()
