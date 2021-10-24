import { setInterval } from "timers";

//uncoment when eventApi be complete 
//import api from "../api.helper";

import { Event } from "../../models/event.model";

//const endpoint = "events";

export class EventService {
  static async getEvents(): Promise<Event[]> {
    //const posts = await api.get<Event[]>(endpoint);
    //return posts;
    const eventList = [
      { id: "1",
        name: "Test pair 1",
        description: "description of 1st pair",
        time: "2021-10-06T08:30:00.000Z",
        type: "Pair" },
      { id: "2",
        name: "Test pair 2",
        description: "description of 2nd pair",
        time: "2021-10-06T10:25:00.000Z",
        type: "Pair" },
      { id: "3",
        name: "Test pair 3",
        description: "description of 3rd pair",
        time: "2021-10-07T08:30:00.000Z",
        type: "Pair" },
    ];
    return new Promise(resolve => {
      setInterval(() => {
        resolve(eventList);
      }, 1000);
    });
  }
}
