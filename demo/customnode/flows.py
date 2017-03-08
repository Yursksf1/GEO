from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow import frontend

from .models import testProcess


@frontend.register
class testFlow(Flow):
    process_class = testProcess

    start = (
        flow.Start(
            CreateProcessView,
            #fields=["text"]
            fields=["text", "email"]
            #fields=["text", "email","date","date2"]
            #fields=["email"]
        ).Permission(
            auto_create=True
        ).Next(this.approve)
    )

    approve = (
        flow.View(
            UpdateProcessView,
            fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_approve)
    )

    check_approve = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.send)
        .Else(this.end)
    )

    send = (
        flow.Handler(
            this.send_hello_world_request1
        ).Next(this.end)
    )

    end = flow.End()

    def send_hello_world_request1(self, activation):
        print(activation.process.text)