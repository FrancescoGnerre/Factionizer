var inputTXT = "";

function toHome(){
  window.location.href = "https://factionizer.bovineghoti.repl.co/";
}
function toSettings(){
  window.location.href = "https://factionizer.bovineghoti.repl.co/settings";
}
function addPlayer() {
  inputTXT = document.getElementById("add_new_player").value;
  console.log(inputTXT);
  alert(inputTXT);
}
function confirmSettings(){
  alert("Confirm these settigns");
}
function clearPlayersAll() {
  alert("TBD");
}
function clearPlayerOne(p_name) {
  alert("Removing " + p_name);
}
function startGame() {
  alert("TBD");
}
function printPlayers() {
   window.location.href = "https://factionizer.bovineghoti.repl.co/listplayers";
}
function printTXT() {
  alert("Printing as TXT");
}
function printPDF() {
  alert("Printing as PDF");
}