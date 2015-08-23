'use strict';

var gulp = require('gulp');
var browserSync = require('browser-sync');
var combiner = require('stream-combiner2');
var reload = browserSync.reload;
var shell = require('gulp-shell');
var less        = require('gulp-less');

// load plugins
var $ = require('gulp-load-plugins')();

var paths = {
  scripts: 'scripts/**/*.js',
  less: 'styles/**/*.less',
  css:  'styles/.compiled',
  images: 'images/**/*',
};


// Compile less into CSS
gulp.task('styles', function() {
    return gulp.src(paths.less)
        .pipe(less())
        .pipe(gulp.dest(paths.css))
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
    gulp.watch(['**/*.html'], reload);

    gulp.watch(paths.less, ['styles']);
    gulp.watch(paths.scripts, ['scripts']);
    gulp.watch(paths.images, ['images']);
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['watch', 'serve', 'styles']);
