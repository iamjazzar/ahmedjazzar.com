
'use strict';

var placeHolder = $( '#place-holder' );
var site = $( document );
var lines = $( 'span' );
var clicks = 0;
var aside = $( '.aside' );

site.keypress(function() {
  var consoleLine = lines.eq(clicks);
  if( clicks >= lines.size()-2 )  {
    return;
  }

  if(clicks >= lines.size()-4)  {
    aside.addClass( 'stretch-left');
    aside.removeClass( 'hide');
  }

  if (clicks === 0) {
    placeHolder.addClass( 'hide' );
  }
  consoleLine.removeClass( 'hide' );
  clicks++;
});
