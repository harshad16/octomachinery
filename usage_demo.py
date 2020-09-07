from octomachinery.app.config import BotAppConfig
from octomachinery.app.github import GitHubApplication
from octomachinery.routing.routers import ConcurrentRouter


router1 = ConcurrentRouter()  # .on and other helpers?

app1 = GitHubApplication(
    event_routers={router1},
    config=BotAppConfig.from_dotenv(),
)


# process many events arriving over HTTP:
__name__ == '__main__' and app1.start()
# [BAD] app1.run()?
# [BAD] app1.serve()?
# [BAD] app1.launch()?
# [BAD] app1.accept_webhooks()?
# [BAD] app1.process_webhooks()?
# [BAD] app1.listen()?
# app1.start()?  <- Probot

# NOTE: Depending on whether the API is for external or internal use,
# NOTE: its semantics may feel different. What for external caller is
# NOTE: "send event into the system", for internals would be "dispatch/
# NOTE: handle the received event".
# process a single event:
# await app1.receive(event)  <- Probot
# await app1.receive_event(event)?
# [BAD] await app1.feed_event(event)?
# [BAD] await app1.dispatch_event(event)?
# [BAD] await app1.dispatch_webhook(event)?  event's more generic than webhook
# [BAD] await app1.consume_event(event)?
# [BAD] await app1.process_event(event)?
# [BAD] await app1.emit_event(event)?
# [BAD] await app1.trigger_event(event)?
# [BAD] await app1.propagate_event(event)?
# [BAD] await app1.accept_event(event)?
# [BAD] await app1.publish_event(event)?
# [BAD] await app1.source_event(event)?
# [BAD] await app1.simulate_event(event)?  <-- tests?  FIXME: have a pytest fixture called `simulate_event`?
# [BAD] await app1.push_event(event)?
# [BAD] await app1.handle_event(event)?
# [BAD] await app1.send_event(event)?
# [BAD] await app1.inject_event(event)?
# [BAD] await app1.make_happen(event)?
# [BAD] await app1.fire_event(event)?
