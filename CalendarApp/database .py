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

    client_name = Column("clientName", String)
    client_email = Column("clientEmail", String)
    client_password = Column("clientPassword", String)

    def __init__(self, client_name, client_email, client_password):
        self.client_name = client_name
        self.client_email = client_email
        self.client_password = client_password

    def __repr__(self):
        return f"Name: {self.client_name} Email: {self.client_email} Password: {self.client_password}"


class GoogleCalendar(Base):
    __tablename__ = "googleCalendars"

    client_event = Column("clientEvent", String)

    def __init__(self, client_event):
        self.client_event = client_event

    def __repr__(self):
        return f"Event: {self.client_event}"


class CalendarEvent(Base):
    __tablename__ = "calendarEvents"

    client_name = Column("clientName", String)
    event_date = Column("eventDate", String)
    summary_text = Column("summaryText", String)
    description = Column("description", String)
    meeting_link = Column("meetingLink", String)

    def __init__(self, client_name, event_date, summary_text, description, meeting_link):
        self.client_name = client_name
        self.event_date = event_date
        self.summary_text = summary_text
        self.description = description
        self.meeting_link = meeting_link

    def __repr__(self):
        return f"Name: {self.client_name} Event: {self.event_date} Text: {self.summary_text} Description: " \
               f"{self.description} Link: {self.meeting_link}"


class ZoomMeeting(Base):
    __tablename__ = "zoomMeetings"

    meeting_sound_record = Column("meetingSoundRecord", String)
    meeting_date = Column("meetingDate", String)

    def __init__(self, meeting_sound_record, meeting_date):
        self.meeting_sound_record = meeting_sound_record
        self.meeting_date = meeting_date

    def __repr__(self):
        return f"Sound record: {self.meeting_sound_record} Date: {self.meeting_date}"


engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

# Start a session
Session = sessionmaker(bind=engine)
session = Session()
