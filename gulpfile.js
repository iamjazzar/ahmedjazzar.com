'use strict';
// generated on 2015-08-28 using generator-gulp-bootstrap3 0.1.5

// Load plugins
var gulp = require('gulp'),
    autoprefixer = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'),
    less = require('gulp-less'),
    jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),
    imagemin = require('gulp-imagemin'),
    rename = require('gulp-rename'),
    rimraf = require('rimraf'),
    coffee = require('gulp-coffee'),
    concat = require('gulp-concat'),
    notify = require('gulp-notify'),
    cache = require('gulp-cache'),
    include = require('gulp-include'),
    gutil = require('gulp-util'),
    rev = require('gulp-rev'),
    revall = require('gulp-rev-all'),
    livereload = require('gulp-livereload'),
    flatten = require('gulp-flatten'),
    browserSync = require('browser-sync'),
    reload = browserSync.reload;

// Define paths
var paths = {
  scripts:   ['static/scripts/*.coffee', 'static/scripts/*.js'],
  styles:    ['static/styles/**/*.less', 'static/styles/**/*.css'],
  images:    ['static/images/*.png'],
  fonts:     ['static/fonts/**/*.{eot,svg,ttf,woff,woff2}']
};

// CSS
gulp.task('css', function() {
  return gulp.src(paths.styles)
    .pipe(less({
      style: 'expanded',
      loadPath: [
        process.cwd() + '/static/styles/partials'
      ]
    }))
    .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
    .pipe(gulp.dest('.compiled/styles'))
    .pipe(rename({suffix: '.min'}))
    .pipe(minifycss())
    .pipe(gulp.dest('.compiled/styles'))
    .pipe(notify({ message: 'CSS task complete' }));
});

// Javascript
gulp.task('js', function() {
  return gulp.src(paths.scripts)
    .pipe(include())
    .pipe(jshint('.jshintrc'))
    .pipe(jshint.reporter('default'))
    .pipe(gulp.dest('.compiled/scripts'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(uglify())
    .pipe(gulp.dest('.compiled/scripts'))
    .pipe(notify({ message: 'JS task complete' }));
});

// Optimize images
gulp.task('images', function() {
  return gulp.src(paths.images)
    .pipe(cache(imagemin({ optimizationLevel: 5, progressive: true, interlaced: true })))
    .pipe(gulp.dest('.compiled/images'))
    //.pipe(rev())
    //.pipe(gulp.dest('.compiled/images'))
    //.pipe(rev.manifest())
    //.pipe(gulp.dest('.'))
    .pipe(notify({ message: 'Images task complete' }));
});

// Clean up
gulp.task('clean', function(cb) {
  rimraf('./compiled', cb);
});

// Rev all files
gulp.task('rev', function () {
  gulp.src('.compiled/**')
    .pipe(revall({ ignore: [/^\/favicon.ico$/g, '.html'] }))
    .pipe(gulp.dest('rev'));
});

// Copy fonts
gulp.task('fonts', function() {
  gulp.src(paths.fonts)
    .pipe(flatten())
    .pipe(gulp.dest('.compiled/fonts'));
});

// Default task
gulp.task('default', ['clean'], function() {
  gulp.start('css', 'js', 'images', 'fonts');
});

// Serve
gulp.task('serve', ['css'], function () {
  browserSync.init(null, {
      proxy: "localhost:8000",
      open: 'internal',
      host: "localhost",
      port: 4000
  });
});

// Watch
gulp.task('watch', ['serve'], function() {

  // Watch LESS files
  gulp.watch(paths.styles, ['css', reload]);

  // Watch JS files
  gulp.watch(paths.scripts, ['js', reload]);

  // Watch image files
  gulp.watch(paths.images, ['images', reload]);

  // Watch html files
  gulp.watch('templates/**/*.html', [reload]);

  // Create LiveReload server
  var server = livereload();

  // Watch any files in assets folder reload on change
  gulp.watch('.compiled/**').on('change', function(file) {
    server.changed(file.path);
  });
});
