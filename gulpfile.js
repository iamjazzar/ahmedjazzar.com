'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var sass = require('gulp-sass');

// Compile sass into CSS & auto-inject into browsers
gulp.task('sass', function () {
  return gulp.src(['static/styles/*.scss'])
    .pipe(sass())
    .pipe(gulp.dest(".compiled/styles/"))
    .pipe(browserSync.stream());
});

// Move the javascript files into our /src/js folder
gulp.task('js', function () {
  return gulp.src(['static/scripts/*.js'])
    .pipe(gulp.dest(".compiled/scripts"))
    .pipe(browserSync.stream());
});

// Static Server + watching scss/html files
gulp.task('serve', ['sass'], function () {

  browserSync.init(null, {
        proxy: "localhost:4500",
        open: "internal",
        host: "localhost",
        port: 3000
    });

  gulp.watch(['static/styles/*.scss'], ['sass']);
  gulp.watch("templates/*.html").on('change', browserSync.reload);
});

gulp.task('default', ['js', 'serve']);
