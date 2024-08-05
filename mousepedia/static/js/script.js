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

document.addEventListener('DOMContentLoaded', function() {
  // initialises the time picker for time_open & time_closed on the add_park form
  let openingTimes = document.querySelectorAll('.timepicker');
  M.Timepicker.init(openingTimes);
});
