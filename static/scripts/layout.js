
'use strict';

var aside = $( '.aside' );
var count = 0;

aside.hover(function() {
  if (count === 0) {
    count++;
    return;
  }
  aside.toggleClass('open', 'slow');
});
