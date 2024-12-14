# Copyright 2021 Agnostiq Inc.
#
# This file is part of Covalent.
#
# Licensed under the Apache License 2.0 (the "License"). A copy of the
# License may be obtained with this software package or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Use of this file is prohibited except in compliance with the License.
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""v12

Revision ID: 26d71848a404
Revises: 9b9d58f02985
Create Date: 2022-09-08 10:46:11.140472

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
# pragma: allowlist nextline secret
revision = "26d71848a404"
# pragma: allowlist nextline secret
down_revision = "9b9d58f02985"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lattices", schema=None) as batch_op:
        batch_op.add_column(sa.Column("docstring_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("deps_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("call_before_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("call_after_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("cova_imports_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("lattice_imports_filename", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("results_dir", sa.Text(), nullable=True))
        batch_op.add_column(sa.Column("root_dispatch_id", sa.String(length=64), nullable=True))

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("lattices", schema=None) as batch_op:
        batch_op.drop_column("root_dispatch_id")
        batch_op.drop_column("results_dir")
        batch_op.drop_column("lattice_imports_filename")
        batch_op.drop_column("cova_imports_filename")
        batch_op.drop_column("call_after_filename")
        batch_op.drop_column("call_before_filename")
        batch_op.drop_column("deps_filename")
        batch_op.drop_column("docstring_filename")

    # ### end Alembic commands ###
