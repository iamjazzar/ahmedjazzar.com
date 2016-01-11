
'use strict';

var main = $( '.main' );
var aside = $( '.aside' );

aside.click(function() {
  $(this).toggleClass('open', 'slow');
});

main.click(function() {
  aside.removeClass('open', 'slow');
});
