from rasa.core.tracker_store import TrackerStore
from rasa.core.trackers import DialogueStateTracker
from typing import Dict, Optional, Text, Any
from sqlalchemy import create_engine, Column, String, Integer, DateTime, Table, MetaData
from sqlalchemy.orm import sessionmaker
from datetime import datetime

class CustomTrackerStore(TrackerStore):
    def __init__(
        self, 
        domain: Optional[Dict[Text, Any]], 
        db_url: Text,
        default_data_db_url: Text,
        table_name: Text = "conversation",
        event_broker=None,
    ) -> None:
        engine = create_engine(db_url)
        self.sessionmaker = sessionmaker(bind=engine)
        metadata = MetaData()

        # Define a new table for users and usage log
        self.user_table = Table(
            'user_usage',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('username', String(100)),
            Column('logged_in_at', DateTime, default=datetime.utcnow),
            Column('logged_out_at', DateTime),
            Column('usage_data', String(1000)),
            Column('session_id', String(100)),
            Column('messages', String(10000)),
        )

        default_data_engine = create_engine(default_data_db_url)
        self.default_data_sessionmaker = sessionmaker(bind=default_data_engine)

        # Define a new table for default data
        self.default_data_table = Table(
            'default_data',
            metadata,
            Column('id', Integer, primary_key=True),
            Column('session_id', String(100)),
            Column('default_data', String(10000)),
        )

        metadata.create_all(engine)
        metadata.create_all(default_data_engine)

        super().__init__(domain, event_broker)

    def save(self, tracker: DialogueStateTracker) -> None:
        if self.event_broker:
            self.stream_events(tracker)

        session = self.sessionmaker()
        user_usage = self.user_table.insert().values(
            username=tracker.get_slot('username'),
            logged_in_at=datetime.utcnow(),
            usage_data=tracker.get_slot('signed_data'),
            session_id=tracker.sender_id,
            messages=str([event.as_dict() for event in tracker.events if event.event != 'action']),
        )
        session.execute(user_usage)
        session.commit()
        session.close()

        default_data_session = self.default_data_sessionmaker()
        default_data = self.default_data_table.insert().values(
            session_id=tracker.sender_id,
            default_data=str([event.as_dict() for event in tracker.events if event.event == 'action']),
        )
        default_data_session.execute(default_data)
        default_data_session.commit()
        default_data_session.close()

    def retrieve(self, sender_id: Text) -> Optional[DialogueStateTracker]:
        # Implement retrieval logic here
        pass