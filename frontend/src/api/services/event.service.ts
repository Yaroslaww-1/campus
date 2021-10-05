import { setInterval } from "timers";

import { Event, DayInWeek, PairTime } from "../../models/event.model";

export class EventService {
  static getEvents(): Promise<Event[]> {
    const eventList = [
      { id: "1",
        name: "Taste pair 1",
        description: "description of 1st pair",
        time: "2021-10-06-T08:30:00.000Z",
        type: "Pair" },
      { id: "2",
        name: "Taste pair 2",
        description: "description of 2nd pair",
        time: "2021-10-06-T10:25:00.000Z",
        type: "Pair" },
      { id: "3",
        name: "Taste pair 3",
        description: "description of 3rd pair",
        time: "2021-10-07-T08:30:00.000Z",
        type: "Pair" },
    ];
    return new Promise(resolve => {
      setInterval(() => {
        resolve(eventList);
      }, 1000);
    });
  }
}

export class DaysInWeek {
  static getDays(): Promise<DayInWeek[]> {
    const daysList = [
      { id: 1, name: "Понеділок" },
      { id: 2, name: "Вівторок" },
      { id: 3, name: "Середа" },
      { id: 4, name: "Четвер" },
      { id: 5, name: "П'ятниця" },
      { id: 6, name: "Субота" },
      { id: 7, name: "Неділя" },
    ];
    return new Promise(resolve => {
      setInterval(() => {
        resolve(daysList);
      }, 1000);
    });
  }
}

export class PairsTime {
  static getPairsTime(): Promise<PairTime[]> {
    const pairList = [
      { id: 1, time: "08:30" },
      { id: 2, time: "10:25" },
      { id: 3, time: "12:20" },
      { id: 4, time: "14:15" },
      { id: 5, time: "16:10" },
      { id: 6, time: "18:30" },
    ];
    return new Promise(resolve => {
      setInterval(() => {
        resolve(pairList);
      }, 1000);
    });
  }
}