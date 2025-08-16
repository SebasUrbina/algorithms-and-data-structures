"""
This is an example that I read in the gook 'Grokking Algorithms'.
It is about to identify actions, calculations and data (ACD)

From page 39 to 53
"""

from pydantic import BaseModel
from enum import StrEnum


class CouponRank(StrEnum):
    BEST = "BEST"
    GOOD = "GOOD"


class Coupon(BaseModel):
    code: str
    rank: CouponRank


class Subscriber(BaseModel):
    email: str
    rec_count: int


class Message(BaseModel):
    from_email: str
    to_email: str
    subject: str
    body: str


def subCouponRank(subscriber: Subscriber) -> Coupon:
    if subscriber.rec_count >= 10:
        return CouponRank.BEST
    else:
        return CouponRank.GOOD


def selectCouponsByRank(coupons: list[Coupon], rank: CouponRank) -> list[str]:
    ret = []

    for coupon in coupons:
        if coupon.rank == rank:
            ret.append(coupon.code)
    return ret


def emailForSubscriber(subscriber: Subscriber, goods: list[str], bests: list[str]) -> Message:

    rank = subCouponRank(subscriber)

    if rank == CouponRank.BEST:
        return Message(
            from_email="newsletter@coupon.co",
            to_email=subscriber.email,
            subject="Your best weekly coupons inside",
            body=f"Here are the best coupons: {', '.join(bests)}",
        )
    if rank == CouponRank.GOOD:
        return Message(
            from_email="newsletter@coupon.co",
            to_email=subscriber.email,
            subject="Your good weekly coupons inside",
            body=f"Here are the good coupons: {', '.join(goods)}",
        )


def emailForSubscribers(
    subscribers: list[Subscriber], goods: list[Coupon], bests: list[Coupon]
) -> list[Message]:
    emails = []
    for subscriber in subscribers:
        email = emailForSubscriber(subscriber, goods, bests)
        emails.append(email)
    return emails


def fetchCouponsFromDB() -> list[Coupon]:
    return [
        Coupon(code="MYCUPONBEST", rank=CouponRank.BEST),
        Coupon(code="MYCUPONGOOD", rank=CouponRank.GOOD),
    ]


def fetchSubscribersFromDB():
    return [
        Subscriber(email="my_mail@mail.com", rec_count=12),
        Subscriber(email="paz@mail.com", rec_count=5),
    ]


class EmailSystem:

    @staticmethod
    def send(email: Message):
        print("Sending email...")
        print(f"From: {email.from_email}")
        print(f"To: {email.to_email}")
        print(f"Subject: {email.subject}")
        print(f"Body: {email.body}")
        return "Email has been sent"


def sendIssue():
    coupons = fetchCouponsFromDB()
    bestCoupons = selectCouponsByRank(coupons, "BEST")
    goodCoupons = selectCouponsByRank(coupons, "GOOD")
    subscribers = fetchSubscribersFromDB()
    emails = emailForSubscribers(subscribers, goodCoupons, bestCoupons)

    email_system = EmailSystem()
    for email in emails:
        email_system.send(email)


sendIssue()
