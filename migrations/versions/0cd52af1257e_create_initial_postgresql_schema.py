"""Create initial PostgreSQL schema"""

from alembic import op
import sqlalchemy as sa


revision = "0cd52af1257e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "admin",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.UniqueConstraint("email"),
    )

    op.create_table(
        "organizations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("organization_name", sa.String(150), nullable=False),
        sa.Column("address", sa.Text(), nullable=False),
        sa.Column("contact_person", sa.String(100), nullable=False),
        sa.Column("phone_number", sa.String(20), nullable=False),
        sa.Column("email", sa.String(120), nullable=False),
        sa.Column("organization_code", sa.String(20), nullable=False),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("organization_code"),
    )

    op.create_table(
        "service_levels",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("service_name", sa.String(100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.UniqueConstraint("service_name"),
    )

    op.create_table(
        "special_needs",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("need_name", sa.String(150), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.UniqueConstraint("need_name"),
    )

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("fullname", sa.String(200), nullable=False),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("role", sa.String(20), nullable=False),
        sa.Column("officer_signature", sa.String(255), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.UniqueConstraint("email"),
    )

    op.create_table(
        "passengers",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("passenger_name", sa.String(100), nullable=False),
        sa.Column("travel_date", sa.Date(), nullable=False),
        sa.Column("position", sa.String(100), nullable=True),
        sa.Column("flight", sa.String(100), nullable=False),
        sa.Column("itinerary", sa.Text(), nullable=True),
        sa.Column("additional_request", sa.Text(), nullable=True),
        sa.Column("date_created", sa.DateTime(), nullable=True),
        sa.Column(
            "organization_id",
            sa.Integer(),
            sa.ForeignKey("organizations.id"),
            nullable=False,
        ),
        sa.Column(
            "service_level_id",
            sa.Integer(),
            sa.ForeignKey("service_levels.id"),
            nullable=False,
        ),
        sa.Column("passenger_signature", sa.String(255), nullable=True),
        sa.Column(
            "user_id",
            sa.Integer(),
            sa.ForeignKey("users.id"),
            nullable=False,
        ),
    )

    op.create_table(
        "passenger_special_needs",
        sa.Column(
            "passenger_id",
            sa.Integer(),
            sa.ForeignKey("passengers.id"),
            primary_key=True,
            nullable=False,
        ),
        sa.Column(
            "special_need_id",
            sa.Integer(),
            sa.ForeignKey("special_needs.id"),
            primary_key=True,
            nullable=False,
        ),
    )


def downgrade():

    op.drop_table("passenger_special_needs")
    op.drop_table("passengers")
    op.drop_table("users")
    op.drop_table("special_needs")
    op.drop_table("service_levels")
    op.drop_table("organizations")
    op.drop_table("admin")