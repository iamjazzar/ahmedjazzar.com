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
  scripts: ['client/js/**/*.coffee', '!client/external/**/*.coffee'],
  less: 'styles/**/*.less',
  css:  'styles/.compiled',
  images: 'client/img/**/*'
};


// Compile less into CSS
gulp.task('styles', function() {
    return gulp.src(paths.less)
        .pipe(less())
        .pipe(gulp.dest(paths.css))
        .pipe(reload({stream: true}));
});

// TODO: Clean task
// TODO: Build task for production

gulp.task('serve', ['styles'], function () {
    browserSync.init(null, {
        proxy: "localhost:8080", // This should be already running in a separate command
        open: 'internal',
        host: "localhost",
        port: 3000
    });
});

gulp.task('watch', ['serve'], function () {
    // watch for changes
    gulp.watch(['**/*.html'], reload);

    gulp.watch('styles/**/*.less', ['styles']);
    gulp.watch('scripts/**/*.js', ['scripts']);
    gulp.watch('images/**/*', ['images']);
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['watch', 'serve', 'styles']);
