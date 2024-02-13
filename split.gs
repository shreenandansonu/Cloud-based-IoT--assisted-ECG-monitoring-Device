function row_split() {
  var ss = SpreadsheetApp.openById('1B5UxbJQ9euV5pNHbRVOFW1cLMwpBMbyf2WzxwmH5AWY');
  var source = ss.getSheetByName('RECORD');
  var destination = ss.getSheetByName('MIN');
  var lastrow = source.getLastRow();
  if (lastrow >= 4) {
    for(let i=lastrow-3;i<=lastrow;i++){
        var value1 = source.getRange(lastrow-3,1).getValue();
        var value2 = source.getRange(lastrow-2,1).getValue();
        var value3 = source.getRange(lastrow-1,1).getValue();
        var value4 = source.getRange(lastrow,1).getValue();
        var mainvalue=value1+value2+value3+value4;
        destination.getRange(1, 1).setValue(mainvalue);
    }
    var range1 = destination.getRange(1, 1);
    range1.splitTextToColumns(' ');
    // var range2 = source.getRange(lastrow - 4, 1);
    // range2.splitTextToColumns(' ');
  }
}