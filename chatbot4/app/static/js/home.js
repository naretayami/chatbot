function get_message() {
    var now_date = new Date();
    var month = now_date.getMonth() + 1;
    return now_date.getFullYear() + "年 " 
    + month + "月 "
    + now_date.getDate() + "日 " 
    + now_date.getHours() + "時 "
    + now_date.getMinutes() + "分 "
    + now_date.getSeconds() + "秒 ";
}
  var nowtime_doc = document.getElementById("nowtime");
  nowtime_doc.innerHTML = "TIME " + get_message();
