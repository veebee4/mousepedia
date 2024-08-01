document.addEventListener('DOMContentLoaded', function() {
  // initialises the side nav bar
  let sidenavbar = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenavbar);
});

document.addEventListener('DOMContentLoaded', function() {
  // initialises the date picker for date_opened on the add_park form 
  let dateOpened = document.querySelectorAll('.datepicker');
  M.Datepicker.init(dateOpened);
  });

  $('.materialize-textarea').val('New Text');
  M.textareaAutoResize($('.materialize-textarea'));
