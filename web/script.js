var ros = new ROSLIB.Ros({
  url: "ws://localhost:9090",
});

ros.on("connection", function () {
  console.log("Connected to websocket server.");
});

ros.on("error", function (error) {
  console.log("Error connecting to websocket server: ", error);
});

ros.on("close", function () {
  console.log("Connection to websocket server closed.");
});
var cmdVelTopic = new ROSLIB.Topic({
  ros: ros,
  name: "chatter",
  messageType: "std_msgs/String",
});
var twist = new ROSLIB.Message({
data: "move"
});
function publish() {

  cmdVelTopic.publish(twist);
  console.log("published");
}

