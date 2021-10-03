import pcqq
import textParser

@pcqq.on_command("/>",aliases=["/》"])
def f(session: pcqq.Session):
  txt = textParser.parse(session.event.MessageText[2:],session.event.UserID)
  session.send(txt)

pcqq.init(3290647713, "1a2B0000000000")
pcqq.run()
