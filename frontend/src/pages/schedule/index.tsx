import { observer } from "mobx-react-lite";
import { useEffect } from "react";

import { eventsState, EventsState } from "./schedule.state";

import { ScheduleTables } from "./components/ScheduleTables";

interface IProps {
  state: EventsState;
}

const EventListContent: React.FC<IProps> = observer(({ state }) => {
  useEffect(()=> {
    state.fetchEvents();
  }, []);
  return(
    <ScheduleTables events={state.events} />
  );
});

export const SchedulePage: React.FC = () => (
  <EventListContent state={eventsState} />
);
