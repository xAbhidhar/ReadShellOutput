from sqlalchemy import Column, Integer, String, BLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Command(Base):
    __tablename__ = "commands"
    id = Column(Integer, primary_key=True)
    command_string = Column(String, nullable=False)
    length = Column(Integer, nullable=False)
    # store duration of command run time in seconds, round up to nearest second
    duration = Column(Integer, nullable=False, default=0)
    output = Column(BLOB)

    def __init__(self, command_string, length, duration, output):
        self.command_string = command_string
        self.length = length
        self.duration = duration
        self.output = output
