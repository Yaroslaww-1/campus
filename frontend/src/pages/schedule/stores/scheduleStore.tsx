type items = {
    id: number;
    weekNumber: number;
    dayIndex: number;
    pairIndex: number;
    isFree: boolean;
    subjName: string;
    teacherName: string;
    typeOfPair: string;
    eventType: string;
    description: string;
};

let scheduleStore: items[] = [];

function tmpSchedule(){
  const tmpObjs: items[] = [];
    
  for (let a=0; a<2; a++){
    for (let i=0; i<7; i++){
      for (let j=0; j<6; j++){
        const tmpHelp = {
          id: (j+i),
          weekNumber:a,
          dayIndex:i,
          pairIndex:j,
          isFree: (Math.random() < 0.5) ? false : true ,
          subjName: "Test",
          teacherName:"Iasd Dfae Herr",
          typeOfPair:"on-line",
          eventType:"lection",
          description:"some text about pair. For example zoom-link",
        };
        tmpObjs.push(tmpHelp);
      }
    }
  }

  //tmpObjs.filter(el => el.weekNumber === 0)
  //tmpObjs.filter(el => el.weekNumber === 1)
  return tmpObjs;
}

scheduleStore = tmpSchedule();

export default scheduleStore;