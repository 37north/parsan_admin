$(document)
    .on('click.bs.dropdown.data-api', '.dropdown', function (e) { e.stopPropagation() })

$(document) 	
  .on('click.my', '.dropdown div', function(e) {
    e.stopPropagation()
  })

  