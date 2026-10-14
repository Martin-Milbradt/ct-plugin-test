"""A test monitor: the packaged simple prompt under its own name."""

from control_tower.monitors.monitor import MonitorFn, prompt_monitor
from control_tower.monitors.registry import monitors


@monitors.register()
def custom_simple(model: str = "") -> MonitorFn:
    """Score each action with the packaged simple prompt."""
    return prompt_monitor("simple", cot_level="none", model=model)
