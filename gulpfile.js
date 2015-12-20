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
    cache = require('gulp-cache'),
    include = require('gulp-include'),
    livereload = require('gulp-livereload'),
    flatten = require('gulp-flatten'),
    browserSync = require('browser-sync'),
    reload = browserSync.reload;

// Define paths
var paths = {
  scripts:   ['static/scripts/*.js'],
  styles:    [
    'static/bower_components/bootstrap/less/bootstrap.less',
    'static/styles/**/*.{less,css}'
   ],
  images:    ['static/images/*.png'],
  fonts:     ['static/fonts/**/*.{eot,svg,ttf,woff,woff2}'],
  bower:     ['static/bower_components/**/*'],
};

// Clean up
gulp.task('clean', function(cb) {
  rimraf('./compiled', cb);
});

gulp.task('bower', function() {
  gulp.src(paths.bower)
    .pipe(gulp.dest('.compiled/bower_components'));
});

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
    .pipe(gulp.dest('.compiled/styles'));
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
    .pipe(gulp.dest('.compiled/scripts'));
});

// Optimize images
gulp.task('images', function() {
  return gulp.src(paths.images)
    .pipe(cache(imagemin({ optimizationLevel: 5, progressive: true, interlaced: true })))
    .pipe(gulp.dest('.compiled/images'));
});

// Copy fonts
gulp.task('fonts', function() {
  gulp.src(paths.fonts)
    .pipe(flatten())
    .pipe(gulp.dest('.compiled/fonts'));
});

// Default task
gulp.task('default', ['clean'], function() {
  gulp.start('css', 'js', 'images', 'fonts', 'bower');
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

  gulp.watch('{ahmedjazzarcom,ahmedjazzar}/**/*.py', function () {
      // TODO: Watch Django Server instead!
      setTimeout(reload, 200);
  });

  // Create LiveReload server
  var server = livereload();

});
