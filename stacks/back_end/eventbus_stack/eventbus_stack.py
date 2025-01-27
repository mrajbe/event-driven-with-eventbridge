import aws_cdk as core
from constructs import Construct
from aws_cdk import aws_events as _evnts


class GlobalArgs:
    """
    Helper to define global statics
    """

    OWNER = "RMAutomation"
    ENVIRONMENT = "production"
    REPO_NAME = "event-driven-with-eventbridge"
    SOURCE_INFO = f"https://github.com/RM/{REPO_NAME}"
    VERSION = "2021_03_06"
    RM_SUPPORT_EMAIL = ["RM@example.com", ]


class EventBusStack(core.Stack):

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        stack_log_level: str,
        **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        id_prefix_str = f"evntDriven"

        self.orders_bus = _evnts.EventBus(
            self,
            "ordersEventBus",
            event_bus_name="store-orders"
        )

        self.orders_bus.apply_removal_policy(
            core.RemovalPolicy.DESTROY
        )

        ###########################################
        ################# OUTPUTS #################
        ###########################################
        output_0 = core.CfnOutput(
            self,
            "AutomationFrom",
            value=f"{GlobalArgs.SOURCE_INFO}",
            description="To know more about this automation stack, check out our github page."
        )

        output_1 = core.CfnOutput(
            self,
            "StoreOrdersEventBus",
            value=f"https://console.aws.amazon.com/events/home?region={core.Aws.REGION}#/eventbus/{self.orders_bus.event_bus_name}",
            description="Orders EventBus"
        )
