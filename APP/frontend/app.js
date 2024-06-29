$(document).ready(function() {
    // Fetch health data
    const fetchHealthData = () => {
        $.ajax({
            url: '/api/health-data',
            method: 'GET',
            success: function(data) {
                // Process and display data in the Dashboard
            },
            error: function(error) {
                console.error('Error fetching health data', error);
            }
        });
    };

    fetchHealthData();

    // Example of handling navigation
    $('a.nav-link').on('click', function(event) {
        event.preventDefault();
        const targetId = $(this).attr('href').substring(1);
        $('html, body').animate({
            scrollTop: $('#' + targetId).offset().top
        }, 500);
    });
});
