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
    clean = require('gulp-clean'),
    coffee = require('gulp-coffee'),
    concat = require('gulp-concat'),
    notify = require('gulp-notify'),
    cache = require('gulp-cache'),
    include = require('gulp-include'),
    ejs = require('gulp-ejs'),
    gutil = require('gulp-util'),
    rev = require('gulp-rev'),
    revall = require('gulp-rev-all'),
    livereload = require('gulp-livereload'),
    gulpif = require('gulp-if'),
    sprite = require('css-sprite').stream,
    flatten = require('gulp-flatten'),
    browserSync = require('browser-sync'),
    reload = browserSync.reload;

// Define paths
var paths = {
  scripts:   ['src/js/*.coffee', 'src/js/*.js'],
  styles:    ['src/css/**/*.less', 'src/css/**/*.css'],
  images:    ['src/images/*.png'],
  fonts:     ['src/**/*.{eot,svg,ttf,woff,woff2}'],
  templates: ['src/templates/*.ejs']
};

// CSS
gulp.task('css', function() {
  return gulp.src(paths.styles)
    .pipe(less({
      style: 'expanded',
      loadPath: [
        process.cwd() + '/src/css/partials',
        process.cwd() + '/src/vendor'
      ]
    }))
    .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
    .pipe(gulp.dest('dist/assets/css'))
    .pipe(rename({suffix: '.min'}))
    .pipe(minifycss())
    .pipe(gulp.dest('dist/assets/css'))
    .pipe(notify({ message: 'CSS task complete' }));
});

// Javascript
gulp.task('js', function() {
  return gulp.src(paths.scripts)
    .pipe(include())
    .pipe(jshint('.jshintrc'))
    .pipe(jshint.reporter('default'))
    .pipe(gulp.dest('dist/assets/js'))
    .pipe(rename({ suffix: '.min' }))
    .pipe(uglify())
    .pipe(gulp.dest('dist/assets/js'))
    .pipe(notify({ message: 'JS task complete' }));
});

// Optimize images
gulp.task('images', function() {
  return gulp.src(paths.images)
    .pipe(cache(imagemin({ optimizationLevel: 5, progressive: true, interlaced: true })))
    .pipe(gulp.dest('dist/assets/images'))
    //.pipe(rev())
    //.pipe(gulp.dest('dist/assets/images'))
    //.pipe(rev.manifest())
    //.pipe(gulp.dest('.'))
    .pipe(notify({ message: 'Images task complete' }));
});

// Templates
gulp.task('templates', function() {
  return gulp.src(paths.templates)
    .pipe(ejs().on('error', gutil.log))
    .pipe(gulp.dest('dist'))
    .pipe(notify({ message: 'Templates task complete' }));
});

// Clean up
gulp.task('clean', function() {
  return gulp.src(['dist/assets/css', 'dist/assets/js', 'dist/assets/images', 'dist/assets/fonts', 'dist/*.html'], {read: false})
    .pipe(clean());
});

// Rev all files
gulp.task('rev', function () {
  gulp.src('dist/**')
    .pipe(revall({ ignore: [/^\/favicon.ico$/g, '.html'] }))
    .pipe(gulp.dest('rev'));
});

// Copy fonts
gulp.task('fonts', function() {
  gulp.src(paths.fonts)
    .pipe(flatten())
    .pipe(gulp.dest('dist/assets/fonts'));
});

// Default task
gulp.task('default', ['clean'], function() {
  gulp.start('css', 'js', 'images', 'templates', 'fonts');
});

// Serve
gulp.task('serve', ['css'], function () {
  browserSync.init(null, {
      proxy: "localhost:7070",
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

  // Watch template files
  gulp.watch(['src/templates/*.ejs', '*.html'], ['templates', reload]);

  // Create LiveReload server
  var server = livereload();

  // Watch any files in assets folder reload on change
  gulp.watch('dist/assets/**').on('change', function(file) {
    server.changed(file.path);
  });

});
