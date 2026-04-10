# app/graphql/schema.py
# Strawberry introspects the Query class and builds the full GraphQL schema.
import strawberry
from app.graphql.resolvers import Query

# Create the GraphQL schema using the Query class defined in resolvers.py, which contains all the field resolvers for our API.
schema = strawberry.Schema(query=Query)
