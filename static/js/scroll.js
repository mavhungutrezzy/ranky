let infinite = new Waypoint.Infinite({
    element: $(".infinite-container")[0],
    handler: function () {},
    offset: "bottom-in-view",

    onBeforePageLoad: function () {
        $(".spinner-border").show();
    },
    onAfterPageLoad: function () {
        $(".spinner-border").hide();
    },
});
