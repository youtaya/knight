if(window.attachEvent) {
  document.getElementById("id_hire_num").onpropertychange = set_alert_wb_comment();
} else {
  document.getElementById("id_hire_num").addEventListener('input', set_alert_wb_comment, false);
}

function set_alert_wb_comment() {
  var address = document.getElementById("id_fact_addr").value;
  // alert("address "+address);
  // 创建地址解析器实例
  var myGeo = new BMap.Geocoder();
  // 将地址解析结果显示在地图上,并调整地图视野
  myGeo.getPoint(address, function(point){
    if (point) {
      var name = document.getElementById("id_fact_name").value;
      document.getElementById("id_fact_lat").value = point.lat;
      document.getElementById("id_fact_lng").value = point.lng;
      alert("lat: "+point.lat + " lng:"+point.lng);
    }else{
      alert("您选择地址没有解析到结果!");
    }
  }, "上海市");
}

function formSubmit() {

}
