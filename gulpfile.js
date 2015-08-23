'use strict';

var gulp = require('gulp');
var less = require('gulp-less');
var shell = require('gulp-shell');
var image = require('gulp-image');
var combiner = require('stream-combiner2');
var browserSync = require('browser-sync');
var reload = browserSync.reload;

// load plugins
var $ = require('gulp-load-plugins')();

var paths = {
  scripts: 'scripts/**/*.js',
  less: 'styles/**/*.less',
  compiled:  '.compiled',
  images: 'images/**/*',
  html: '**/*.html',
};

gulp.task('styles', function() {
    return gulp.src(paths.less)
        .pipe(less())
        .pipe(gulp.dest(paths.compiled))
        .pipe(reload({stream: true}));
});

gulp.task('serve', ['styles'], function () {
    browserSync.init(null, {
        proxy: "localhost:7070",
        open: 'internal',
        host: "localhost",
        port: 4000
    });
});

gulp.task('watch', ['serve'], function () {
    // watch for changes
    gulp.watch([paths.html], reload);
    gulp.watch(paths.less, ['styles']);
    gulp.watch(paths.images, ['images']);
    // gulp.watch(paths.scripts, ['scripts']);
});

gulp.task('images', function () {
  gulp.src(paths.images)
    .pipe(image())
    .pipe(gulp.dest(paths.compiled));
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['watch', 'serve', 'styles', 'images']);
