
'use strict';

var aside = $( '.aside' );
var main = $( '.main' );
var triggered = false;

aside.hover(function() {
  aside.addClass('open', 'slow');
  triggered=true;
});

main.hover(function() {
  if (triggered) {
    aside.removeClass('open', 'slow');
  }
});

main.click(function() {
  aside.toggleClass('open', 'slow');
});
