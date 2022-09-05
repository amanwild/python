var wait = (delay, ...args) => new Promise(resolve => setTimeout(resolve, delay, ...args));
var fb_dtsg = "CHANGE_THIS"; //Required
var notToRemoveIds = ["ID1", "ID2", "ID3", "..."] //Optional

var getFriendIds = function() {
  var ids = [];
  var frList = document.getElementsByClassName('_698');
  for (i = 0; i < frList.length; i++) {
    var id = frList[i].querySelectorAll('div > div > div > div > div > button')[1].getAttribute('data-profileid');
    ids.push(id);
  }
  return ids;
}

var makeRemoveCall = async (uid, fb_dtsg) => {
  await wait(1000);
  var http = new XMLHttpRequest();
  var url = 'https://www.facebook.com/ajax/profile/removefriendconfirm.php';
  var params = "uid=" + uid + "&fb_dtsg=" + fb_dtsg;
  http.open('POST', url, false);
  http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');

  http.onreadystatechange = function() {
    if (http.readyState == 4 && http.status == 200) {
      console.log("Removed friend with ID: " + uid);
    }
  }
  http.send(params);
};

async function removeFriends() {
  console.log("Friend removal started");
  var ids = getFriendIds();
  for (i = 0; i < ids.length; i++) {
    if (!notToRemoveIds.includes(ids[i])) {
        await makeRemoveCall(ids[i], fb_dtsg);
    }
  }
  console.log("Friend removal completed");
}

removeFriends();