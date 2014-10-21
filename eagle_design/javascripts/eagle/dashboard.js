// sum function
sum = function (list, end) {
    // This only works with an ordered list of lists
    for(var s=0,i=end+1;i;s+=list[--i][1]);
    return s;
}
// I still don't understand javascript for loops.
newsum = function (list) { for (var total=0,i=list.length;i;total +=list[--i][1]);return total;}

var today = new Date();
var weekago = new Date(today.getTime()-1000*60*60*24*7);
var monthago = new Date(today.getTime()-1000*60*60*24*30);

intros_last_week = Array();
intros_last_month = Array();
intros_all_time = Array();
_.each(INTRO_TOTALS.Intros_Made, function(item,index,list) {if (item[0] * 1000 > weekago.getTime()) {intros_last_week.push([item[0] * 1000,item[1]])}});
_.each(INTRO_TOTALS.Intros_Made, function(item,index,list) {if (item[0] * 1000 > monthago.getTime()) {intros_last_month.push([item[0] * 1000,item[1]])}});
_.each(INTRO_TOTALS.Intros_Made, function(item,index,list) {intros_all_time.push([item[0] * 1000,item[1]])});

received_last_week = Array();
received_last_month = Array();
received_all_time = Array();
_.each(INTRO_TOTALS.Intros_Received, function(item,index,list) {if (item[0] * 1000 > weekago.getTime()) {received_last_week.push([item[0] * 1000,item[1]])}});
_.each(INTRO_TOTALS.Intros_Received, function(item,index,list) {if (item[0] * 1000 > monthago.getTime()) {received_last_month.push([item[0] * 1000,item[1]])}});
_.each(INTRO_TOTALS.Intros_Received, function(item,index,list) {received_all_time.push([item[0] * 1000,item[1]])});


var GRAPH_DATA = [
    {   title: "Made",
        subtitle: "Last Week",
        headline: newsum(intros_last_week),
        selector_id: "intros-made-this-week",
        data: {label: "made",
            data: intros_last_week
        }
    },
    {   title: "Received",
        subtitle: "Last Week",
        headline: newsum(received_last_week),
        selector_id: "intros-received-this-week",
        data: {label: "received",
            data:received_last_week
        }
    },
    {   title: "Made",
        subtitle: "Last Month",
        headline: newsum(intros_last_month),
        selector_id: "intros-made-last-week",
        data: {label: "made",
            data: intros_last_month
        }
    },
    {   title: "Received",
        subtitle: "Last Month",
        headline: newsum(received_last_month),
        selector_id: "intros-received-last-week",
        data: {label: "received",
            data: received_last_month
        }
    },
    {   title: "Made",
        subtitle: "All Time",
        headline: newsum(intros_all_time),
        selector_id: "intros-made-all-time",
        data: {label: "made",
            data: intros_all_time
        }
    },
    {   title: "Received",
        subtitle: "All Time",
        headline: newsum(received_all_time),
        selector_id: "intros-received-all-time",
        data: {label: "received",
            data: received_all_time
        }
    }
];

$( document ).ready(function() {


  //-Mustache Template
  var template = '<h4>{{headline}}<span>{{title}}</span></h4><div class="bar-chart"></div><h3>{{subtitle}}</h3>';

  //-Plot Settings (Line Chart)
  //-lines: { show: false }, xaxis: {show: false}, yaxis: {show: false}
  var options = {
    series: {
        stack: 0,
        color: '#aed981',
        lines: { show: true, steps: false },
        bars: { show: true, fill: true, fillColor: '#aed981', barWidth: 0.9 }
    },
    grid: { hoverable: true, borderWidth: 0, show: true },
    tooltip: true,
    tooltipOpts: {
        content: "%y %s on %x",
        xDateFormat: "%b %e",
    },
    legend: {
      show: false,
    },
    xaxis: {
      show: true,
      color: '#ffffff',
      mode: 'time',
    },
    yaxis:  {
      show: true,
      color: '#ffffff',
    }
  };

  _.each(GRAPH_DATA, function(item,index,list) {

    //item.data.data = intros_last_week;
    //item.data.label = "Intros Received";
    //item.headline = intros_last_week.length;

    var output = Mustache.to_html(template, item);
    document.getElementById(item.selector_id).innerHTML = output;

    //var DATA_set = Array();
    //DATA_set = item.data;
    //_.each(item.data, function(item,index,list) {DATA_set.push([item[0] * 1000, item[1]])});

    $.plot($('#' + item.selector_id + ' .bar-chart'), [ item.data ], options);

  });

})
