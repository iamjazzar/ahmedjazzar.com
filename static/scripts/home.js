
'use strict';

var placeHolder = $( '#place-holder' );
var site = $( document );
var lines = $( '#console span' );
var aside = $( '.aside' );
var alertContainer = $( '.alert-container' );
var canAlert = true;
var clicks = 0;
var skipped = false;
var screenMd = 992;

function skipMe() {
  if(skipped) {
    return;
  }

  setInterval(function(){
    site.trigger( 'keypress', 71 );
  },40);
}

function showAlert() {
  alertContainer.removeClass( 'hide' );
  alertContainer.addClass( 'fast-enter' );
}

function hideAlert() {
  alertContainer.addClass( 'fadeout' );
  alertContainer.addClass( 'hide' );
  alertContainer.removeClass( 'fast-enter' );
}

site.keydown(function(e) {
  var keyCode = e.keyCode || e.which;
  if (keyCode === 9) {
    e.preventDefault();
    hideAlert();
    skipMe();
  }
});

site.keypress(function() {
  var consoleLine = lines.eq(clicks);
  if( clicks >= lines.size()-2 )  {
    return;
  }

  if(clicks >= lines.size()-4)  {
    aside.addClass( 'slide-left');
    aside.removeClass( 'hide');
  }

  if (clicks === 0) {
    placeHolder.addClass( 'hide' );
  }

  if(clicks === 3)  {
    hideAlert();
    canAlert = false;
  }
  consoleLine.removeClass( 'hide' );
  clicks++;
});

site.click(function() {

  if (canAlert) {
    showAlert();
  }
});

if ($(window).width() < screenMd) {
   skipMe();
}
