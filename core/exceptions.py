class BotError(Exception):
    """Base class for all bot-specific exceptions."""
    pass


# ==========================
# User Errors
# ==========================

class UserError(BotError):
    """Base class for errors caused by user actions."""
    pass


class PermissionDenied(UserError):
    """Raised when the user lacks permission to perform an action."""
    pass


class InvalidArgument(UserError):
    """Raised when a user provides an invalid argument."""
    pass


class CooldownError(UserError):
    """Raised when a command is still on cooldown."""
    pass


class NotFoundError(UserError):
    """Raised when a requested resource cannot be found."""
    pass


# ==========================
# Service Errors
# ==========================

class ServiceError(BotError):
    """Base class for service-related failures."""
    pass


class APIError(ServiceError):
    """Raised when an API request fails or returns an unexpected response."""
    pass


class DatabaseError(ServiceError):
    """Raised when a database operation fails."""
    pass


class ExternalServiceError(ServiceError):
    """Raised when an external third-party service fails."""
    pass


# ==========================
# System Errors
# ==========================

class ConfigurationError(BotError):
    """Raised when the bot configuration is missing or invalid."""
    pass


class InternalError(BotError):
    """Raised when an unexpected internal error occurs."""
    pass
