
'use strict';

var placeHolder = $( '#place-holder' );
var site = $( document );
var lines = $( '#console span' );
var aside = $( '.aside' );
var clicks = 0;
var skipped = false;

function skipMe() {
  if(skipped) {
    return;
  }

  setInterval(function(){
    site.trigger( 'keypress', 71 );
  },40);
}

site.keydown(function(e) {
  var keyCode = e.keyCode || e.which;
  if (keyCode === 9) {
    e.preventDefault();
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
  consoleLine.removeClass( 'hide' );
  clicks++;
});
