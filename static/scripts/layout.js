
'use strict';

var aside = $( '.aside' );
var main = $( '.main' );
var count = 0;

aside.hover(function() {
  aside.addClass('open', 'slow');
});

main.hover(function() {
  if (count === 0) {
    count++;
    return;
  }
  aside.removeClass('open', 'slow');
});

main.click(function() {
  aside.toggleClass('open', 'slow');
});
