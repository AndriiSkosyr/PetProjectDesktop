from sqlalchemy import create_engine, ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# class Thing(Base):
#    __tablename__ = "things"
#
#    tid = Column("tid", Integer, primary_key=True)
#    description = Column("description", String)
#    owner = Column(Integer, ForeignKey("people.ssn"))
#
#    def __init__(self, tid, description, owner):
#        self.tid = tid
#        self.description = description
#        self.owner = owner
#
#   def __repr__(self):
#        return f"({self.tid}) {self.description} owned by {self.owner}"


class Client(Base):
    __tablename__ = "clients"

    # defining the fields of the row
    client_id = Column("clientId", Integer, primary_key=True)
    client_name = Column("clientName", String)
    client_email = Column("clientEmail", String)
    client_password = Column("clientPassword", String)

    # class constructor
    def __init__(self, client_id, client_name, client_email, client_password):
        self.client_id = client_id
        self.client_name = client_name
        self.client_email = client_email
        self.client_password = client_password

    # function to output the table
    def __repr__(self):
        return f"ID: ({self.client_id}) Name: /{self.client_name}/ Email: /{self.client_email}/ " \
               f"Password: /{self.client_password}/"


class GoogleCalendar(Base):
    __tablename__ = "googleCalendars"

    calendar_id = Column("calendarId", Integer, primary_key=True)
    client_event = Column("clientEvent", String)

    def __init__(self, calendar_id, client_event):
        self.calendar_id = calendar_id
        self.client_event = client_event

    def __repr__(self):
        return f"ID: ({self.calendar_id}) Event: /{self.client_event}/"


class CalendarEvent(Base):
    __tablename__ = "calendarEvents"

    event_id = Column("eventId", Integer, primary_key=True)
    client_name = Column("clientName", String)
    event_date = Column("eventDate", String)
    summary_text = Column("summaryText", String)
    description = Column("description", String)
    meeting_link = Column("meetingLink", String)

    def __init__(self, event_id, client_name, event_date, summary_text, description, meeting_link):
        self.event_id = event_id
        self.client_name = client_name
        self.event_date = event_date
        self.summary_text = summary_text
        self.description = description
        self.meeting_link = meeting_link

    def __repr__(self):
        return f"ID: ({self.event_id}) Name: /{self.client_name}/ Event: /{self.event_date}/ " \
               f"Text: /{self.summary_text}/ Description: " \
               f"/{self.description}/ Link: /{self.meeting_link}/"


class ZoomMeeting(Base):
    __tablename__ = "zoomMeetings"

    meeting_id = Column("meetingId", Integer, primary_key=True)
    meeting_sound_record = Column("meetingSoundRecord", String)
    meeting_date = Column("meetingDate", String)

    def __init__(self, meeting_id, meeting_sound_record, meeting_date):
        self.meeting_id = meeting_id
        self.meeting_sound_record = meeting_sound_record
        self.meeting_date = meeting_date

    def __repr__(self):
        return f"ID: ({self.meeting_id}) Sound record: /{self.meeting_sound_record}/ Date: /{self.meeting_date}/"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

# Start a session
Session = sessionmaker(bind=engine)
session = Session()


# functions to insert data into database
def insert_client(object_name, client_id, client_name, client_email, client_password):
    object_name = Client(client_id, client_name, client_email, client_password)
    session.add(object_name)
    session.commit()


def insert_google_calendar(object_name, calendar_id, client_event):
    object_name = GoogleCalendar(calendar_id, client_event)
    session.add(object_name)
    session.commit()


def insert_calendar_event(object_name, event_id, client_name, event_date, summary_text, description, meeting_link):
    object_name = CalendarEvent(event_id, client_name, event_date, summary_text, description, meeting_link)
    session.add(object_name)
    session.commit()


def insert_zoom_meeting(object_name, meeting_id, meeting_sound_record, meeting_date):
    object_name = ZoomMeeting(meeting_id, meeting_sound_record, meeting_date)
    session.add(object_name)
    session.commit()


# functions to output data from database
def print_clients():
    clients = session.query(Client)
    for client in clients:
        print(client)


def print_google_calendars():
    calendars = session.query(GoogleCalendar)
    for calendar in calendars:
        print(calendar)


def print_calendar_events():
    events = session.query(CalendarEvent)
    for event in events:
        print(event)


def print_zoom_meetings():
    meetings = session.query(ZoomMeeting)
    for meeting in meetings:
        print(meeting)
